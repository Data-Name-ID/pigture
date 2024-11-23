import { Metadata } from "next";
import LoginForm from "@/components/login-form";

export const metadata: Metadata = {
    title: "Авторизоваться",
    description: "Войдите в систему для доступа к лабораторным изображениям",
};

export default function LoginPage() {
    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center bg-[url('/lab-background.svg')] bg-cover bg-center">
            <LoginForm />
        </div>
    );
}
