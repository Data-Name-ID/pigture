import { redirect } from "next/navigation";
import { ImagesWrapper } from "./components/imagesWrapper";
import { config } from "@/config";
import { ImageCard } from "./components/imageCard";
import { getAccessToken } from "@/lib-f/auth";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export interface DjangoQueryResponse {
    count: number;
    results: Result[];
}

export interface Result {
    id: number;
    author: number;
    name: string;
    file: string;
    description: string;
    uploaded_at: Date;
    category: string | null;
    tiles: string | null;
}

export default async function Dashboard({ searchParams }: { searchParams: Promise<{ page?: string }> }) {
    const page = (await searchParams).page;
    const accessToken = await getAccessToken();

    if (!accessToken) redirect("/");

    const q = page ?? "1";
    const resp = await fetch(`${config.API}/images?page=${q}`, {
        headers: {
            Authorization: `Bearer ${accessToken}`,
        },
    });

    if (!resp.ok) {
        return <h1>500 Server Crashed :(</h1>;
    }

    const data: DjangoQueryResponse = await resp.json();

    return (
        <div className="flex min-h-screen w-full">
            <ul className="hidden w-1/4 bg-muted/40 p-6 md:flex flex-col gap-4">
                <Link href={"/dashboard/upload"} className="w-full">
                    <Button variant={"default"}>Загрузить</Button>
                </Link>
            </ul>
            <ImagesWrapper>
                {data.results.map((image) => (
                    <ImageCard key={image.id} {...image} />
                ))}
            </ImagesWrapper>
        </div>
    );
}
