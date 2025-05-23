"use client";

import { useState, useEffect } from "react";
import { DynamicIcon } from "lucide-react/dynamic";
import { colors, gradients } from "./theme";

interface Item {
  id: number;
  name: string;
  description: string | null;
}

export default function Home() {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };

    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  const [items] = useState<Item[]>([
    {
      id: 1,
      name: "Item 1",
      description: "Description for item 1",
    },
    {
      id: 2,
      name: "Item 2",
      description: "Description for item 2",
    },
    {
      id: 3,
      name: "Item 3",
      description: "Description for item 3",
    },
  ]);

  return (
    <main className="min-h-screen p-8 relative">
      <div
        className={`absolute inset-0 bg-gradient-to-tr ${gradients.main} animate-gradient-x`}
      ></div>
      <div
        className="fixed inset-0 bg-black/65 pointer-events-none z-20"
        style={{
          background: `radial-gradient(circle 175px at ${mousePosition.x}px ${mousePosition.y}px, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0) 60%, rgba(0, 0, 0, 0.45) 100%)`,
        }}
      />
      <div className="relative z-10">
        <h1 className="text-4xl font-bold mb-8 text-white">
          Next.js + FastAPI Demo
        </h1>
        <DynamicIcon name={"guitar"} color={colors.text.primary} size={32} />
        <div className="flex flex-col gap-6">
          {items.map((item) => (
            <div
              key={item.id}
              className="p-8 bg-black/20 backdrop-blur-sm rounded-lg shadow-md hover:shadow-lg transition-all duration-300 text-white w-full hover:bg-black/30 hover:shadow-[0_0_15px_rgba(255,255,255,0.1)]"
            >
              <h2 className="text-2xl font-semibold mb-4">{item.name}</h2>
              <p className="text-gray-200 text-lg">{item.description}</p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
