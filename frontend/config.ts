export const config = {
    API: "http://87.251.74.161:8000",
    DEV_TEMP: (addr: string) => {
        const s = addr.replace("http://87.251.74.161", config.API);
        return s;
    },
};
