"use client";

import { FormEvent, useRef, useState } from "react";
import { Button } from "./ui/button";
import { AlertCircle, CheckCircle2, LoaderCircle } from "lucide-react";

import axiosInstance from "./utils/axiosInstance";
import toast from "react-hot-toast";

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

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setSelectedFile(e.target.files[0]);
        }
    };

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();

        if (!selectedFile) {
            toast.error("Выберите файл.");
            return;
        }

        const formData = new FormData();
        formData.append("image", new Blob([selectedFile]), selectedFile.name);

        try {
            await axiosInstance
                .post("http://localhost:8000/images/upload/", formData, {
                    headers: { "Access-Control-Allow-Origin": "*" },
                    onUploadProgress: (progressEvent) => {
                        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total!);
                        setUploadState((prev) => ({ ...prev, progress: percentCompleted }));
                    },
                })
                .catch((err) => {
                    toast.error(`Ошибка: ${err}`);
                });

            setUploadState((prev) => ({ ...prev, success: true }));
            setSelectedFile(null);
        } catch (error) {
            toast.error(`Ошибка: ${error}`);
        } finally {
            setSelectedFile(null);
        }
    };

    return (
        <form className="w-full max-w-md mx-auto p-6 flex flex-col gap-4" onSubmit={handleSubmit}>
            <input type="file" ref={fileInputRef} onChange={handleFileChange} className="hidden" />
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
            {uploadState.progress > 0 && (
                <div className="fixed right-4 top-4 z-10 ">
                    <LoaderCircle className="w-full animate-spin h-12">0%</LoaderCircle>
                    <span className="text-sm absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">{uploadState.progress}%</span>
                </div>
            )}
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
