"use client";

import { useState, useEffect } from "react";

function useWindowSize() {
    const [windowSize, setWindowSize] = useState({
        innerWidth: typeof window !== "undefined" ? window.innerWidth : 0,
        innerHeight: typeof window !== "undefined" ? window.innerHeight : 0,
    });

    useEffect(() => {
        function handleResize() {
            setWindowSize({
                innerWidth: window.innerWidth,
                innerHeight: window.innerHeight,
            });
        }

        window.addEventListener("resize", handleResize);

        handleResize();

        return () => window.removeEventListener("resize", handleResize);
    }, []);

    return windowSize;
}

export default useWindowSize;
