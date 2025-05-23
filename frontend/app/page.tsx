"use client";

import { useState, useEffect, useRef } from "react";
import { DynamicIcon } from "lucide-react/dynamic";
import { colors, gradients } from "./theme";

interface Item {
  id: number;
  name: string;
  description: string | null;
}

export default function Home() {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [flashlightSize, setFlashlightSize] = useState(175);
  const [isAnimating, setIsAnimating] = useState(false);
  const animationRef = useRef<number>();

  const animateFlashlight = (
    startSize: number,
    endSize: number,
    duration: number
  ) => {
    if (animationRef.current) {
      cancelAnimationFrame(animationRef.current);
    }

    const startTime = performance.now();

    const animate = (currentTime: number) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Fonction d'easing plus simple et plus fiable
      const easeProgress =
        progress < 0.5
          ? 2 * progress * progress
          : 1 - Math.pow(-2 * progress + 2, 2) / 2;

      const currentSize = startSize + (endSize - startSize) * easeProgress;
      setFlashlightSize(currentSize);

      if (progress < 1) {
        animationRef.current = requestAnimationFrame(animate);
      } else {
        animationRef.current = undefined;
      }
    };

    animationRef.current = requestAnimationFrame(animate);
  };

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };

    const handleClick = () => {
      if (!isAnimating) {
        setIsAnimating(true);
        // Animation d'agrandissement
        animateFlashlight(175, 500, 1000);

        // Animation de rétrécissement après un délai
        setTimeout(() => {
          animateFlashlight(500, 175, 1000);
          setTimeout(() => {
            setIsAnimating(false);
          }, 1000);
        }, 1000);
      }
    };

    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("click", handleClick);
    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("click", handleClick);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
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
    <main className="min-h-screen p-20 relative">
      <div
        className={`absolute inset-0 bg-gradient-to-tr ${gradients.main} animate-gradient-x`}
      ></div>
      <div
        className="fixed inset-0 bg-black/65 pointer-events-none z-20"
        style={{
          background: `radial-gradient(circle ${flashlightSize}px at ${mousePosition.x}px ${mousePosition.y}px, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0) 60%, rgba(0, 0, 0, 0.45) 100%)`,
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
              className="p-8 bg-black/20 backdrop-blur-sm rounded-lg shadow-md hover:shadow-lg transition-[height,transform,box-shadow] duration-1000 ease-in-out text-white w-full hover:bg-black/10 hover:shadow-[0_0_30px_rgba(255,255,255,0.25)] text-center h-[150px] hover:h-[300px] hover:z-10 relative group"
            >
              <h2 className="text-2xl font-semibold mb-4">{item.name}</h2>
              <p className="text-gray-200 text-lg">{item.description}</p>
              <button className="absolute bottom-4 left-1/2 -translate-x-1/2 bg-white/10 hover:bg-white/20 px-6 py-2 rounded-full transition-all duration-500 opacity-0 group-hover:opacity-100 scale-0 group-hover:scale-100">
                En savoir plus
              </button>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
