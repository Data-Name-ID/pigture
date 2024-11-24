"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { MicroscopeIcon } from "lucide-react";
import { useRouter } from "next/navigation";
import axios, { HttpStatusCode } from "axios";
import toast from "react-hot-toast";
import { getAccessToken } from "@/lib/auth";

export type JWTRequestPayload = {
    username: string;
    password: string;
};

export default function LoginForm() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post(`/api/auth/token`, {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${await getAccessToken()}`,
                },
                body: JSON.stringify({ username, password } as JWTRequestPayload),
            });
            if (response.status === HttpStatusCode.Ok) {
                router.push("/dashboard");
            } else {
                toast.error("Ошибка на сервере.");
            }
        } catch (err) {
            console.error(err);
            toast.error("Что-то не так с браузером.");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <Card className="w-[380px] backdrop-blur-sm bg-white/80">
                <CardHeader className="space-y-1">
                    <div className="flex items-center justify-center mb-2">
                        <MicroscopeIcon className="h-12 w-12 text-blue-500" />
                    </div>
                    <CardTitle className="text-2xl text-center">Программа просмотра лабораторных изображений</CardTitle>
                    <CardDescription className="text-center">Введите свои учетные данные для доступа к лабораторным изображениям</CardDescription>
                </CardHeader>
                <CardContent className="grid gap-4">
                    <div className="grid gap-2">
                        <Label htmlFor="username">Имя пользователя</Label>
                        <Input
                            id="username"
                            type="text"
                            placeholder="Введите свое имя пользователя"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                    </div>
                    <div className="grid gap-2">
                        <Label htmlFor="password">Пароль</Label>
                        <Input
                            id="password"
                            type="password"
                            placeholder="Введите свой пароль"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                </CardContent>
                <CardFooter>
                    <Button className="w-full bg-blue-500 hover:bg-blue-600" onClick={handleSubmit}>
                        Авторизоваться
                    </Button>
                </CardFooter>
            </Card>
        </form>
    );
}
