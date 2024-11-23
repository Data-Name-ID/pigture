import { JWTRequestPayload } from "@/components/login-form";
import { config } from "@/config";
import { NextRequest, NextResponse } from "next/server";

type DjangoJWTResp = {
    access: string;
    refresh: string;
};

export async function POST(request: NextRequest) {
    try {
        const req = await request.json();
        const { username, password } = JSON.parse(req.body) as JWTRequestPayload;

        const djangoResponse = await fetch(`${config.API}/token/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        if (!djangoResponse.ok) {
            const errorData = await djangoResponse.json();
            console.error(errorData);
            return NextResponse.json(errorData, { status: djangoResponse.status });
        }

        const data: DjangoJWTResp = await djangoResponse.json();
        const response = new NextResponse();

        response.cookies.set("accessToken", data.access, {
            httpOnly: false,
            secure: process.env.NODE_ENV === "production",
            maxAge: 30 * 60,
            path: "/",
            sameSite: "strict",
        });

        response.cookies.set("refreshToken", data.refresh, {
            httpOnly: false,
            secure: process.env.NODE_ENV === "production",
            maxAge: 60 * 60 * 24 * 7,
            path: "/",
            sameSite: "strict",
        });

        return response;
    } catch (error) {
        console.error("Error:", error);
        return NextResponse.json({ detail: "Internal Server Error" }, { status: 500 });
    }
}
