"use client";

// IMPLEMENT REFRESH TOKEN API!
export const apiClient = async (url = "", options = {}) => {
    const response = await fetch(url, {
        ...options,
        credentials: "include",
    });

    if (response.status === 401) {
        const refreshResponse = await fetch("/api/refresh-token", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({}),
            credentials: "include",
        });

        if (refreshResponse.ok) {
            return fetch(url, {
                ...options,
                credentials: "include",
            });
        } else {
            window.location.href = "/";
            return;
        }
    }

    return response;
};
