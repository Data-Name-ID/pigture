import { Metadata } from "next";
import LoginForm from "@/components/login-form";

export const metadata: Metadata = {
    title: "Авторизоваться",
    description: "Войдите в систему для доступа к лабораторным изображениям",
};

export default function LoginPage() {
    return (
        <div className="min-h-screen w-full  flex items-center justify-center">
            <LoginForm />
        </div>
    );
}
