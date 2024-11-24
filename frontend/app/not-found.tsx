import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function NotFound() {
    return (
        <div className="min-h-screen flex flex-col items-center justify-center p-4">
            <div className="max-w-md w-full text-center">
                <svg
                    className="w-48 h-48 mx-auto mb-8"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                >
                    <path d="M10 2v7.31" />
                    <path d="M14 9.3V1.99" />
                    <path d="M8.5 2h7" />
                    <path d="M14 9.3a6.5 6.5 0 1 1-4 0" />
                    <path d="M5.58 16.5h12.85" />
                </svg>
                <h1 className="text-4xl font-bold mb-4">Упс! Что-то не так!</h1>
                <p className="text-xl text-gray-600 mb-8"> Приношу вам извинения... Мы уже начали разработать над ошибкой.</p>
                <Button asChild>
                    <Link href="/dashboard">Панель управления</Link>
                </Button>
            </div>
        </div>
    );
}
