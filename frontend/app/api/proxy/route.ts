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
