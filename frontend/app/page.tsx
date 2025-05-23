"use client";

import { DynamicIcon } from "lucide-react/dynamic";
import { colors } from "./theme";
import { FlashlightEffect } from "./components/FlashlightEffect";
import { Background } from "./components/Background";
import { Footer } from "./components/Footer";
import { eagleLake, outfit } from "./fonts";
import Categories from "./components/Categories";

export default function Home() {
  return (
    <main className={`min-h-screen p-20 relative ${outfit.className}`}>
      <Background />
      <FlashlightEffect>
        <div className="relative z-10">
          <h1
            className={`text-5xl font-bold mb-8 ${eagleLake.className} text-center 
              bg-gradient-to-r from-[#DBAF19] to-[#FFD700] bg-clip-text text-transparent
              [text-shadow:_0_0_15px_#DBAF19]
              [animation:_pulse_3s_ease-in-out_infinite]`}
          >
            Lumyons
          </h1>
          <p className="text-xl text-center mb-12 text-gray-200 font-medium tracking-wide">
            Eclaires ta culture de Lyon.
          </p>
          <Categories />
          <Footer />
        </div>
      </FlashlightEffect>
    </main>
  );
}
