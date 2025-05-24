import { smooch } from "../fonts";
import { Heart, Github } from "lucide-react";
import { colors } from "../theme";

export const Footer = () => {
  return (
    <footer className="mt-20 text-center">
      <p className="text-m text-center text-gray-200 font-medium tracking-wide">
        <a href="/about" className="hover:text-white transition-colors">
          A propos
        </a>
        {" • "}
        <a
          href="https://github.com/444chak/24hinfo_web"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-white transition-colors inline-flex items-center gap-1"
        >
          <Github className="w-4 h-4" />
          GitHub
        </a>
      </p>
      <br />
      <p className={`${smooch.className} text-2xl text-white/80 select-none`}>
        Made with{" "}
        <Heart
          className="inline-block w-6 h-6 mx-2"
          style={{ color: colors.text.tertiary }}
        />
        by Antislash N
      </p>
      <p className="text-sm text-white/60 mt-2">
        © {new Date().getFullYear()} - All rights reserved
      </p>
    </footer>
  );
};
