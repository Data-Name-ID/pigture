export const config = {
    API: "http://87.251.74.156:8000",
    DEV_TEMP: (addr: string) => {
        const s = addr.replace("http://87.251.74.156", config.API);
        return s;
    },
};
