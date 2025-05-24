import { useState, useEffect, useRef } from "react";
import { Eye, EyeOff, MousePointerClick } from "lucide-react";

interface FlashlightEffectProps {
  children: React.ReactNode;
  isEnabled?: boolean;
}

export const FlashlightEffect = ({
  children,
  isEnabled = true,
}: FlashlightEffectProps) => {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [flashlightSize, setFlashlightSize] = useState(175);
  const [isAnimating, setIsAnimating] = useState(false);
  const [isEnabledLocal, setIsEnabledLocal] = useState(true);
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

    let timeoutId: NodeJS.Timeout;
    let shrinkTimeoutId: NodeJS.Timeout;

    const handleClick = () => {
      if (timeoutId) clearTimeout(timeoutId);
      if (shrinkTimeoutId) clearTimeout(shrinkTimeoutId);

      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
        animationRef.current = undefined;
      }

      setIsAnimating(true);
      animateFlashlight(175, 500, 1000);

      timeoutId = setTimeout(() => {
        animateFlashlight(500, 175, 1000);
        shrinkTimeoutId = setTimeout(() => {
          setIsAnimating(false);
        }, 1000);
      }, 1000);
    };

    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("click", handleClick);
    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("click", handleClick);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
      if (timeoutId) clearTimeout(timeoutId);
      if (shrinkTimeoutId) clearTimeout(shrinkTimeoutId);
    };
  }, []);

  return (
    <>
      <button
        onClick={() => setIsEnabledLocal(!isEnabledLocal)}
        className="fixed top-4 right-4 z-30 bg-white/10 hover:bg-white/20 p-2 rounded-full transition-all duration-300"
        title={isEnabledLocal ? "Désactiver le masque" : "Activer le masque"}
      >
        {isEnabledLocal ? (
          <EyeOff className="w-6 h-6 text-white" />
        ) : (
          <Eye className="w-6 h-6 text-white" />
        )}
      </button>
      <button
        onClick={() => setIsEnabledLocal(!isEnabledLocal)}
        className="fixed top-20 right-4 z-30 bg-white/10 hover:bg-white/20 p-2 rounded-full transition-all duration-300"
        title="Click gauche pour agrandir la lumière"
      >
        <MousePointerClick className="w-6 h-6 text-white" />
      </button>
      {isEnabled && isEnabledLocal && (
        <div
          className="fixed inset-0 bg-black/65 pointer-events-none z-20"
          style={{
            background: `radial-gradient(circle ${flashlightSize}px at ${mousePosition.x}px ${mousePosition.y}px, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0) 60%, rgba(0, 0, 0, 0.45) 100%)`,
          }}
        />
      )}
      {children}
    </>
  );
};
