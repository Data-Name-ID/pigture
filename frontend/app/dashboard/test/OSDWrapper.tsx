"use client";

import dynamic from "next/dynamic";

const OpenSeadragonViewer = dynamic(() => import("../../../components/osd"), { ssr: false });

export function OSDWrapper() {
    const tileSource = "/1.dzi";

    return (
        <div>
            <OpenSeadragonViewer tileSource={tileSource} width="800px" height="600px" />
        </div>
    );
}
