// "use client";

import { useEffect, useRef } from "react";
import OpenSeadragon from "openseadragon";
import useWindowSize from "@/app/dashboard/view/components/adjust";

const OpenSeadragonViewer = ({ tileSource }: { tileSource: OpenSeadragon.Options["tileSources"]; width?: string; height?: string }) => {
    const viewerRef = useRef(null);
    const osdInstance = useRef<OpenSeadragon.Viewer | null>(null);

    useEffect(() => {
        if (viewerRef.current && !osdInstance.current) {
            osdInstance.current = OpenSeadragon({
                element: viewerRef.current,
                tileSources: tileSource,
                prefixUrl: "/",
                navImages: {
                    zoomIn: {
                        DOWN: "zoom-in.svg",
                        GROUP: "zoom-in.svg",
                        HOVER: "zoom-in.svg",
                        REST: "zoom-in.svg",
                    },
                    zoomOut: {
                        DOWN: "zoom-out.svg",
                        GROUP: "zoom-out.svg",
                        HOVER: "zoom-out.svg",
                        REST: "zoom-out.svg",
                    },
                    home: {
                        DOWN: "home.svg",
                        GROUP: "home.svg",
                        HOVER: "home.svg",
                        REST: "home.svg",
                    },
                    fullpage: {
                        DOWN: "fullscreen.svg",
                        GROUP: "fullscreen.svg",
                        HOVER: "fullscreen.svg",
                        REST: "fullscreen.svg",
                    },
                    flip: {
                        DOWN: "flip.svg",
                        GROUP: "flip.svg",
                        HOVER: "flip.svg",
                        REST: "flip.svg",
                    },
                    next: {
                        DOWN: "next-img.svg",
                        GROUP: "next-img.svg",
                        HOVER: "next-img.svg",
                        REST: "next-img.svg",
                    },
                    previous: {
                        DOWN: "prev-img.svg",
                        GROUP: "prev-img.svg",
                        HOVER: "prev-img.svg",
                        REST: "prev-img.svg",
                    },
                    rotateleft: {
                        DOWN: "rotate-ccw.svg",
                        GROUP: "rotate-ccw.svg",
                        HOVER: "rotate-ccw.svg",
                        REST: "rotate-ccw.svg",
                    },
                    rotateright: {
                        DOWN: "rotate-cw.svg",
                        GROUP: "rotate-cw.svg",
                        HOVER: "rotate-cw.svg",
                        REST: "rotate-cw.svg",
                    },
                },
                showNavigator: true,
            });
        }

        return () => {
            if (osdInstance.current) {
                osdInstance.current.destroy();
                osdInstance.current = null;
            }
        };
    }, [tileSource]);

    const { innerWidth, innerHeight } = useWindowSize();

    return <div ref={viewerRef} style={{ width: innerWidth, height: innerHeight }}></div>;
};

export default OpenSeadragonViewer;
