import { gradients } from "../theme";

interface BackgroundProps {
  gradient?: keyof typeof gradients;
}

export const Background = ({ gradient = "main" }: BackgroundProps) => {
  return (
    <div
      className={`absolute inset-0 bg-gradient-to-tr ${gradients[gradient]} animate-gradient-x`}
    />
  );
};
