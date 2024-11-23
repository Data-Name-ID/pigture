"use client";

import { useState, useEffect } from "react";
import { Progress } from "@/components/ui/progress";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Upload, CheckCircle, XCircle } from "lucide-react";
import toast from "react-hot-toast";

interface FileUploadProgressProps {
    fileName: string;
    fileSize: number;
    progress: number;
}

export default function FileUploadProgress({ fileName, fileSize, progress }: FileUploadProgressProps) {
    const [bytesTransferred, setBytesTransferred] = useState(0);
    const [transferRate, setTransferRate] = useState(0);
    const [status, setStatus] = useState<"uploading" | "completed" | "error">("uploading");

    useEffect(() => {
        const startTime = Date.now();
        let lastUpdateTime = startTime;
        let lastBytesTransferred = 0;

        const updateProgress = () => {
            const currentBytes = Math.round((progress / 100) * fileSize);
            setBytesTransferred(currentBytes);

            const now = Date.now();
            const timeDiff = (now - lastUpdateTime) / 1000;
            if (timeDiff >= 1) {
                const bytesDiff = currentBytes - lastBytesTransferred;
                setTransferRate(bytesDiff / timeDiff);
                lastUpdateTime = now;
                lastBytesTransferred = currentBytes;
            }

            if (progress === 100) {
                setStatus("completed");
                toast.success("Загрузка закончилась.");
            }
        };
        updateProgress();
    }, [fileSize, progress]);

    const formatBytes = (bytes: number) => {
        if (bytes === 0) return "0 Bytes";
        const k = 1024;
        const sizes = ["Bytes", "KB", "MB", "GB", "TB"];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
    };

    const formatTransferRate = (bytesPerSecond: number) => {
        return `${formatBytes(bytesPerSecond)}/s`;
    };

    return (
        <Card className="w-full max-w-md">
            <CardHeader>
                <CardTitle className="text-lg font-semibold flex items-center gap-2">
                    {status === "uploading" && <Upload className="w-5 h-5 text-blue-500 animate-pulse" />}
                    {status === "completed" && <CheckCircle className="w-5 h-5 text-green-500" />}
                    {status === "error" && <XCircle className="w-5 h-5 text-red-500" />}
                    {fileName}
                </CardTitle>
            </CardHeader>
            <CardContent>
                <div className="space-y-2">
                    <Progress value={progress} className="w-full" />
                    <div className="text-sm text-gray-500 space-y-1">
                        <p>
                            {formatBytes(bytesTransferred)} / {formatBytes(fileSize)} ({progress.toFixed(1)}%)
                        </p>
                        <p>Transfer Rate: {formatTransferRate(transferRate)}</p>
                        <p className="font-medium">Status: {status.charAt(0).toUpperCase() + status.slice(1)}</p>
                    </div>
                </div>
            </CardContent>
        </Card>
    );
}
