"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { ArrowLeft } from "lucide-react";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

interface CulturalItem {
  id: number;
  name: string;
  description: string;
  image_url: string;
  category_id: number;
  coordinates?: {
    latitude: number;
    longitude: number;
  };
}

export default function CategoryPage() {
  const params = useParams();
  const router = useRouter();
  const [items, setItems] = useState<CulturalItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [categoryName, setCategoryName] = useState<string>("");

  useEffect(() => {
    const fetchCategoryAndItems = async () => {
      try {
        // Fetch category details
        const categoryResponse = await fetch(
          `${API_BASE_URL}/api/categories/${params.id}`
        );
        if (!categoryResponse.ok) {
          const errorData = await categoryResponse.json().catch(() => null);
          throw new Error(errorData?.detail || "Failed to fetch category");
        }
        const categoryData = await categoryResponse.json();
        setCategoryName(categoryData.name);

        // Fetch cultural items for this category
        const itemsResponse = await fetch(
          `${API_BASE_URL}/api/cultural-items/category/${params.id}`
        );
        if (!itemsResponse.ok) {
          const errorData = await itemsResponse.json().catch(() => null);
          throw new Error(
            errorData?.detail || "Failed to fetch cultural items"
          );
        }
        const itemsData = await itemsResponse.json();
        setItems(itemsData);
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    fetchCategoryAndItems();
  }, [params.id]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black">
        <div className="container mx-auto px-4 py-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[1, 2, 3].map((index) => (
              <div
                key={index}
                className="bg-black/20 backdrop-blur-sm rounded-lg p-4 animate-pulse"
              >
                <div className="h-48 bg-white/10 rounded-lg mb-4" />
                <div className="h-6 bg-white/10 rounded w-3/4 mb-2" />
                <div className="h-4 bg-white/10 rounded w-full" />
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black flex items-center justify-center">
        <div className="text-red-500 text-center p-8 bg-black/20 backdrop-blur-sm rounded-lg">
          {error}
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 to-black">
      <div className="container mx-auto px-4 py-8">
        <button
          onClick={() => router.back()}
          className="flex items-center gap-2 text-white hover:text-gray-300 transition-colors mb-8 group"
        >
          <ArrowLeft className="w-5 h-5 group-hover:-translate-x-1 transition-transform" />
          Retour
        </button>

        <h1 className="text-4xl font-bold mb-8 text-white bg-gradient-to-r from-blue-500 to-purple-500 bg-clip-text text-transparent">
          {categoryName}
        </h1>

        <div className="text-gray-400 mb-6">
          {items.length} {items.length === 1 ? "élément" : "éléments"} dans
          cette catégorie
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {items.map((item) => (
            <div
              key={item.id}
              className="bg-black/20 backdrop-blur-sm rounded-lg overflow-hidden hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1 p-6"
            >
              <h2 className="text-xl font-semibold text-white mb-3">
                {item.name}
              </h2>
              <p className="text-gray-300 mb-4">{item.description}</p>
              <div className="text-sm text-gray-400">
                <p>ID: {item.id}</p>
                <p>Catégorie ID: {item.category_id}</p>
                {item.coordinates && (
                  <a
                    href={`https://www.google.com/maps?q=${item.coordinates.latitude},${item.coordinates.longitude}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-400 hover:text-blue-300 transition-colors mt-2 inline-block"
                  >
                    Voir sur Google Maps
                  </a>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
