import { NextRequest, NextResponse } from "next/server";

export async function middleware(req: NextRequest) {
    const url = req.nextUrl.clone();
    const accessToken = req.cookies.get("accessToken")?.value;

    const protectedPaths = ["/dashboard"];

    if (protectedPaths.some((path) => url.pathname.startsWith(path))) {
        if (!accessToken) {
            url.pathname = "/";
            return NextResponse.redirect(url);
        }
    }

    return NextResponse.next();
}

export const config = {
    matcher: ["/dashboard/:path*"],
};
