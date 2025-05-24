import { Eagle_Lake, Outfit, Smooch } from "next/font/google";

export const eagleLake = Eagle_Lake({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export const outfit = Outfit({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-outfit",
});

export const smooch = Smooch({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});
