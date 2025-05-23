import { gradients } from "../theme";

export const Background = () => {
  return (
    <div
      className={`absolute inset-0 bg-gradient-to-tr ${gradients.main} animate-gradient-x`}
    />
  );
};
