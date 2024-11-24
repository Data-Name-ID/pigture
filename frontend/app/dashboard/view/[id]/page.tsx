import { notFound } from "next/navigation";
import { OSDWrapper } from "../components/OSDWrapper";
import { config } from "@/config";
import { getAccessToken } from "@/lib-f/auth";
import { Result } from "../../page";

export default async function View({ params }: { params: Promise<{ id: string }> }) {
    const id = (await params).id;
    if (!id) {
        return notFound();
    }
    const resp = await fetch(`${config.API}/images/${id}`, {
        headers: {
            Authorization: `Bearer ${await getAccessToken()}`,
        },
    });
    if (!resp.ok) {
        return <h1>Что-то не так с сервером :(</h1>;
    }
    const data: Result = await resp.json();
    if (!data.tiles) {
        return notFound();
    }
    return (
        <div>
            <OSDWrapper {...data} />
        </div>
    );
}
