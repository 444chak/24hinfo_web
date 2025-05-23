"use client";

import { useEffect, useState } from "react";
import { DynamicIcon } from "lucide-react/dynamic";

interface Category {
  id: number;
  name: string;
  description: string;
  icon: string;
  primary: string;
}

export default function Categories() {
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await fetch("/api/categories/");
        if (!response.ok) {
          throw new Error("Failed to fetch categories");
        }
        const data = await response.json();
        setCategories(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    fetchCategories();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-[200px]">
        Loading...
      </div>
    );
  }

  if (error) {
    return <div className="text-red-500 text-center">{error}</div>;
  }

  return (
    <div className="flex flex-col gap-6">
      {categories.map((category) => (
        <div
          key={category.id}
          className="p-8 bg-black/20 backdrop-blur-sm rounded-lg shadow-md hover:shadow-lg transition-[height,transform,box-shadow] duration-1000 ease-in-out text-white w-full hover:bg-black/10 hover:shadow-[0_0_30px_rgba(255,255,255,0.25)] text-center h-[150px] hover:h-[200px] hover:z-10 relative group"
        >
          <div className="flex items-center justify-center mb-4">
            <div
              className="w-12 h-12 rounded-full flex items-center justify-center mr-4"
              style={{ backgroundColor: category.primary }}
            >
              {/* @ts-ignore */}
              <DynamicIcon name={category.icon} color="black" size={24} />
            </div>
            <h2 className="text-2xl font-semibold">{category.name}</h2>
          </div>
          <p className="text-gray-200 text-lg">{category.description}</p>
          <button className="absolute bottom-4 left-1/2 -translate-x-1/2 bg-white/10 hover:bg-white/20 px-6 py-2 rounded-full transition-all duration-500 opacity-0 group-hover:opacity-100 scale-0 group-hover:scale-100">
            Découvrir {category.name}
          </button>
        </div>
      ))}
    </div>
  );
}
