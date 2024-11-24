import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { Toaster } from "react-hot-toast";

const geistSans = localFont({
    src: "./fonts/GeistVF.woff",
    variable: "--font-geist-sans",
    weight: "100 900",
});
const geistMono = localFont({
    src: "./fonts/GeistMonoVF.woff",
    variable: "--font-geist-mono",
    weight: "100 900",
});

export const metadata: Metadata = {
    title: "Pigture",
    description: "Pigture",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
                <Toaster position="bottom-right" />
                <div className="min-h-screen grid">
                    <main className="flex flex-col gap-8 items-center bg-gray-100 bg-[url('/lab-background.svg')] bg-cover bg-center">
                        {children}
                    </main>
                </div>
            </body>
        </html>
    );
}
