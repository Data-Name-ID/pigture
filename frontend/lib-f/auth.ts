"use server";

import { cookies } from "next/headers";
import { NextResponse } from "next/server";

export const getAccessToken = async () => {
    const cookieStore = await cookies();
    return cookieStore.get("accessToken")?.value;
};

export const getRefreshToken = async () => {
    const cookieStore = await cookies();
    return cookieStore.get("refreshToken")?.value;
};

export const removeTokens = async () => {
    const cookie = await cookies();
    const accessTokenCookie = cookie.set("accessToken", "", {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        maxAge: -1,
        path: "/",
        sameSite: "strict",
    });

    const refreshTokenCookie = cookie.set("refreshToken", "", {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        maxAge: -1,
        path: "/",
        sameSite: "strict",
    });

    return new NextResponse(null, {
        status: 200,
        headers: {
            "Set-Cookie": `${accessTokenCookie}; ${refreshTokenCookie}`,
        },
    });
};
