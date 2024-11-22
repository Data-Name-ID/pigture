"use client";

import dynamic from "next/dynamic";

const OpenSeadragonViewer = dynamic(() => import("../../../components/osd"), { ssr: false });

export function OSDWrapper() {
    const tileSource = `/api/proxy?url=${encodeURIComponent(`${process.env.DJANGO_API}/1.dzi`)}`;
    return (
        <div>
            <OpenSeadragonViewer tileSource={tileSource} width="800px" height="600px" />
        </div>
    );
}
