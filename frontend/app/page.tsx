"use client";

import { DynamicIcon } from "lucide-react/dynamic";
import { colors } from "./theme";
import { FlashlightEffect } from "./components/FlashlightEffect";
import { Background } from "./components/Background";
import { Footer } from "./components/Footer";
import { eagleLake, outfit } from "./fonts";
import Categories from "./components/Categories";
import { motion } from "framer-motion";

export default function Home() {
  return (
    <main
      className={`min-h-screen p-4 sm:p-8 md:p-12 lg:p-20 relative ${outfit.className}`}
    >
      <Background />
      <FlashlightEffect>
        <motion.div
          className="relative z-10"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <motion.h1
            className={`text-5xl font-bold mb-8 ${eagleLake.className} text-center select-none
              bg-gradient-to-r from-[#DBAF19] to-[#FFD700] bg-clip-text text-transparent
              [text-shadow:_0_0_15px_#DBAF19]
              [animation:_pulse_3s_ease-in-out_infinite]`}
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            Lumyons
          </motion.h1>
          <motion.p
            className="text-xl text-center mb-12 text-gray-200 font-medium tracking-wide"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.4 }}
          >
            Eclaires ta culture de Lyon.
          </motion.p>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.6 }}
          >
            <Categories />
          </motion.div>
          <Footer />
        </motion.div>
      </FlashlightEffect>
    </main>
  );
}
