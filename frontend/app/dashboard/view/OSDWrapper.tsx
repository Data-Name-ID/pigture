"use client";

import dynamic from "next/dynamic";

const OpenSeadragonViewer = dynamic(() => import("../../../components/osd"), { ssr: false });

export function OSDWrapper() {
    const tileSource = `/api/proxy?url=${encodeURIComponent(`http://127.0.0.1:8080/1.dzi`)}`;
    // const tileSource = `/api/proxy?url=${encodeURIComponent(`${process.env.DJANGO_API}/1.dzi`)}`;
    // const tileSource = "http://127.0.0.1:8080/1.dzi";
    return (
        <div>
            <OpenSeadragonViewer tileSource={tileSource} width="1400px" height="900px" />
        </div>
    );
}
