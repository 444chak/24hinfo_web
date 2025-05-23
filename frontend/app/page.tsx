"use client";

import { useState } from "react";
import { DynamicIcon } from "lucide-react/dynamic";
import { colors } from "./theme";
import { FlashlightEffect } from "./components/FlashlightEffect";
import { ItemCard } from "./components/ItemCard";
import { Background } from "./components/Background";
import { Footer } from "./components/Footer";
import { eagleLake, outfit } from "./fonts";

interface Item {
  id: number;
  name: string;
  description: string | null;
}

export default function Home() {
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
    <main className={`min-h-screen p-20 relative ${outfit.className}`}>
      <Background />
      <FlashlightEffect>
        <div className="relative z-10">
          <h1
            className={`text-4xl font-bold mb-8 text-white ${eagleLake.className}`}
          >
            Lumyons
          </h1>
          <DynamicIcon name={"guitar"} color={colors.text.primary} size={32} />
          <div className="flex flex-col gap-6">
            {items.map((item) => (
              <ItemCard key={item.id} item={item} />
            ))}
          </div>
          <Footer />
        </div>
      </FlashlightEffect>
    </main>
  );
}
