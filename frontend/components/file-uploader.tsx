"use client";

import { ChangeEvent, FormEvent, useRef, useState } from "react";
import { Button } from "./ui/button";
import { AlertCircle, CheckCircle2 } from "lucide-react";

import toast from "react-hot-toast";
import { Input } from "./ui/input";
import { Label } from "./ui/label";
import FileUploadProgress from "./file-upload-progress";
import axios from "axios";

interface UploadState {
    progress: number;
    error: string | null;
    success: boolean;
}

export function FileUploader() {
    const fileInputRef = useRef<HTMLInputElement>(null);
    const [uploadState, setUploadState] = useState<UploadState>({
        progress: 0,
        error: null,
        success: false,
    });

    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [filename, setFilename] = useState<string | null>(null);

    const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setSelectedFile(e.target.files[0]);
            setFilename(e.target.files[0].name);
        }
    };
    const handleFilenameChange = (e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.value && selectedFile) {
            setFilename(e.target.value);
        }
    };
    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();

        if (!selectedFile) {
            toast.error("Выберите файл.");
            return;
        }
        if (!filename) {
            toast.error("Некорректное файловое имя.");
            return;
        }
        const fileExtension = selectedFile.name.split(".").pop();
        if (!fileExtension) {
            toast.error("Запрященный файл.");
            return;
        }
        if (!filename.endsWith(fileExtension)) {
            toast.error("Расширение не совпадают.");
            return;
        }

        const formData = new FormData();

        formData.append("name", filename);
        formData.append("file", new Blob([selectedFile]), filename);

        try {
            const response = (await axios
                .postForm(`/api/proxy`, formData, {
                    headers: { Authorization: `Bearer ${document.cookie.split(";")[0].split("=")[1]}` },
                    onUploadProgress: (progressEvent) => {
                        const percentCompleted = progressEvent.total ? (progressEvent.loaded / progressEvent.total) * 100 : 0;
                        setUploadState((prev) => ({ ...prev, progress: percentCompleted }));
                    },
                })
                .catch((err) => {
                    toast.error(`Ошибка: ${err}`);
                })) as { statusText: string };
            toast.success(response["statusText"]);
            setUploadState((prev) => ({ ...prev, success: true }));
            setSelectedFile(null);
        } catch (error) {
            toast.error(`Ошибка: ${error}`);
        } finally {
            setSelectedFile(null);
            setFilename(null);
        }
    };

    return (
        <form className="w-full max-w-md mx-auto p-6 flex flex-col gap-4" onSubmit={handleSubmit}>
            {selectedFile && filename && uploadState.progress > 0 && (
                <FileUploadProgress fileName={filename} fileSize={selectedFile.size} progress={uploadState.progress} />
            )}
            {filename && (
                <>
                    <Label htmlFor="filname">Имя файла:</Label>
                    <Input type="text" value={filename} onChange={handleFilenameChange} id="filename" />
                </>
            )}
            <Input type="file" ref={fileInputRef} onChange={handleFileChange} className="hidden" />
            <Button
                type="button"
                onClick={() => {
                    fileInputRef.current?.click();
                }}
                disabled={uploadState.progress > 0 && uploadState.progress < 100}
            >
                {uploadState.progress > 0 && uploadState.progress < 100 ? "Загрузка..." : "Выберите файл для загрузки"}
            </Button>
            <Button disabled={!Boolean(selectedFile)} onClick={handleSubmit} type="submit">
                Загрузить
            </Button>

            {uploadState.error && (
                <div className="flex items-center space-x-2 text-red-500">
                    <AlertCircle size={16} />
                    <p className="text-sm">{uploadState.error}</p>
                </div>
            )}
            {uploadState.success && (
                <div className="flex items-center space-x-2 text-green-500">
                    <CheckCircle2 size={16} />
                    <p className="text-sm">Файл успешно загружен!</p>
                </div>
            )}
        </form>
    );
}
