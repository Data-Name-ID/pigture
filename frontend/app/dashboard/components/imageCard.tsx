import Image from "next/image";
import { Result } from "../page";
import { config } from "@/config";
import Link from "next/link";

type ImageCardProps = Result;

export function ImageCard({ description, id, name, file }: ImageCardProps) {
    return (
        <Link key={id} className="aspect-square overflow-hidden" title={description} href={`/dashboard/view/${id}`}>
            <Image
                src={config.DEV_TEMP(file).replace(".tif", ".png")}
                alt={name}
                width={300}
                height={300}
                className="object-cover w-full h-full transition-transform hover:scale-105"
            />
        </Link>
    );
}
