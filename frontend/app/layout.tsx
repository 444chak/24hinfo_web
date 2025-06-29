import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Lumyons",
  description: "Regardez la culture lyonnaise sous les projecteurs",
  icons: {
    icon: "/favicon.ico",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-gray-100">{children}</body>
    </html>
  );
}
