import { config } from "@/config";
import axios from "axios";
import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
    const { searchParams } = new URL(request.url);
    const url = searchParams.get("url");
    if (!url) {
        return new Response(JSON.stringify({ error: "URL is required" }), {
            status: 400,
            headers: { "Content-Type": "application/json" },
        });
    }

    console.log(url);

    try {
        const response = await axios.get(url, {
            responseType: "stream",
        });
        const headers = {
            "Content-Type": response.headers["content-type"] || "application/octet-stream",
        };
        return new Response(response.data, { status: 200, headers });
    } catch (error) {
        console.error("Proxy Error:", error);

        return new Response(JSON.stringify({ error: "Failed to fetch resource" }), {
            status: 500,
            headers: { "Content-Type": "application/json" },
        });
    }
}

export async function POST(request: NextRequest) {
    const authHeader = request.headers.get("Authorization");
    if (!authHeader) {
        return new Response(JSON.stringify({ Error: "No authorization header." }), { status: 400, headers: { "Content-Type": "application/json" } });
    }
    const headers: Record<string, string> = {};
    for (const [k, v] of request.headers.entries()) headers[k] = v;
    const response = await fetch(`${config.API}/images/`, {
        method: "POST",
        headers: headers,
        body: request.body,
        duplex: "half",
    } as RequestInit);
    if (!response.ok) {
        return new Response(JSON.stringify({ Error: `Unable to pipe request to ${config.API}` }));
    }
    return response;
}
