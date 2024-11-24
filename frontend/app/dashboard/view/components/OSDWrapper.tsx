"use client";

import dynamic from "next/dynamic";
import { Result } from "../../page";
import { config } from "@/config";

const OpenSeadragonViewer = dynamic(() => import("../../../../components/osd"), { ssr: false });

type OSDWrapperProps = Result;

export function OSDWrapper({ tiles }: OSDWrapperProps) {
    if (!tiles) return <h1>Не удалось загрузить...</h1>;
    const tileSource = `/api/proxy?url=${encodeURIComponent(`${config.DEV_TEMP(tiles)}`)}`;
    return <OpenSeadragonViewer tileSource={tileSource} />;
}
