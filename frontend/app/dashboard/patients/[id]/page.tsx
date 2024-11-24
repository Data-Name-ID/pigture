import { notFound } from "next/navigation";

export default async function PatientsView({ params }: { params: Promise<{ id: string }> }) {
    const id = (await params).id;
    if (!id) {
        return notFound();
    }
    return <></>;
}
