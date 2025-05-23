import { smooch } from "../fonts";
import { Heart } from "lucide-react";

export const Footer = () => {
  return (
    <footer className="mt-20 text-center">
      <p className={`${smooch.className} text-2xl text-white/80`}>
        Made with <Heart className="inline-block w-6 h-6 text-red-500 mx-2" />
        by Antislash N
      </p>
      <p className="text-sm text-white/60 mt-2">
        © {new Date().getFullYear()} - All rights reserved
      </p>
    </footer>
  );
};
