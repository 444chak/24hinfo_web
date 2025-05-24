"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import { Background } from "../components/Background";
import { FlashlightEffect } from "../components/FlashlightEffect";
import { Modal } from "../components/Modal";
import { Footer } from "../components/Footer";
import { motion } from "framer-motion";

export default function AboutPage() {
  const params = useParams();
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [categoryName, setCategoryName] = useState<string>("");
  const [isMaskEnabled, setIsMaskEnabled] = useState(true);

  return (
    <div className="min-h-screen relative">
      <Background />
      <FlashlightEffect>
        <div className="container mx-auto px-4 py-8 relative z-10">
          <motion.button
            onClick={() => router.back()}
            className="flex items-center gap-2 text-white hover:text-gray-300 transition-colors mb-8 group"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5 }}
          >
            <ArrowLeft className="w-5 h-5 group-hover:-translate-x-1 transition-transform" />
            Retour
          </motion.button>
          <motion.h1
            className="text-4xl font-bold mb-8 text-white bg-gradient-to-r from-[#D35400] via-[#E67E22] to-[#F39C12] bg-clip-text text-transparent"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            A propos
          </motion.h1>
          <motion.p
            className="text-lg text-white mb-4"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
          >
            Bonjour jeune jury !
            <br />
            Ce site propose une expérience interactive autour de la découverte
            de différentes cultures lyonaises. Naviguez à travers les pages pour
            explorer, apprendre et interagir avec les fonctionnalités proposées.
            L’interface met l’accent sur l’accessibilité, l’animation et la
            simplicité d’utilisation pour offrir une navigation agréable et
            intuitive.
            <br />
            Nous avons pensé à vos yeux à 6h00 du matin, en intégrant un mode
            sombre avec une lampe de poche pour éclairer votre chemin.
            <br />
            En espérant vous avoir fait découvrir votre propre ville sous un
            autre angle, nous vous souhaitons une bonne visite !
          </motion.p>
          <br />
          <motion.h2
            className="text-2xl font-bold mb-4 text-white bg-gradient-to-r from-[#D35400] via-[#E67E22] to-[#F39C12] bg-clip-text text-transparent"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.6 }}
          >
            Qui sommes-nous ?
          </motion.h2>
          <motion.p
            className="text-lg text-white mb-4"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.8 }}
          >
            Nous sommes l'équipe \n, composée de 2 étudiants en 3ème année de
            BUT Info à Vélizy et de 2 étudiants en 1ère année de BUT Info à
            Vélizy.
          </motion.p>
          <br />
          <motion.h2
            className="text-2xl font-bold mb-4 text-white bg-gradient-to-r from-[#D35400] via-[#E67E22] to-[#F39C12] bg-clip-text text-transparent"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.6 }}
          >
            Stack technique
          </motion.h2>
          <motion.ul
            className="list-disc list-inside text-lg text-white mb-4"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.8 }}
          >
            <li>Next.js</li>
            <li>TypeScript</li>
            <li>Tailwind CSS</li>
            <li>FastApi</li>
            <li>SqlLite</li>
          </motion.ul>
          <br />
          <motion.p
            className="text-lg text-white mb-4 italic"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.8 }}
          >
            PS: Ce site à été réalisé dans le cadre des 24h de l'info de 2025 à
            Lyon 1.
          </motion.p>
          <Footer />
        </div>
      </FlashlightEffect>
    </div>
  );
}
