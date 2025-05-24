"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import { Background } from "../../components/Background";
import { FlashlightEffect } from "../../components/FlashlightEffect";
import { Modal } from "../../components/Modal";
import { Footer } from "../../components/Footer";
import { motion } from "framer-motion";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "https://lumyons.chkb.fr/api";

interface CulturalItem {
  id: number;
  name: string;
  description: string;
  images: string;
  gmaps: string;
  category_id: number;
  address: string;
  arrondissement: string;
}

export default function CategoryPage() {
  const params = useParams();
  const router = useRouter();
  const [items, setItems] = useState<CulturalItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [categoryName, setCategoryName] = useState<string>("");
  const [selectedItem, setSelectedItem] = useState<CulturalItem | null>(null);
  const [isMaskEnabled, setIsMaskEnabled] = useState(true);

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
      <div className="min-h-screen relative">
        <Background />
        <div className="container mx-auto px-4 py-8 relative z-10">
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
      <div className="min-h-screen relative flex items-center justify-center">
        <Background />
        <div className="text-red-500 text-center p-8 bg-black/20 backdrop-blur-sm rounded-lg relative z-10">
          {error}
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen relative">
      <Background />
      <FlashlightEffect isEnabled={isMaskEnabled}>
        <motion.div
          className="container mx-auto px-4 py-8 relative z-10"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
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
            className="text-4xl font-bold mb-8 text-white bg-gradient-to-r from-blue-500 to-purple-500 bg-clip-text text-transparent"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            {categoryName}
          </motion.h1>

          <motion.div
            className="text-gray-400 mb-6"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.3 }}
          >
            {items.length} {items.length === 1 ? "élément" : "éléments"} dans
            cette catégorie
          </motion.div>

          <motion.div
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5, delay: 0.4 }}
          >
            {items.map((item, index) => (
              <motion.div
                key={item.id}
                onClick={() => {
                  setSelectedItem(item);
                  setIsMaskEnabled(false);
                }}
                className="bg-black/20 backdrop-blur-sm rounded-lg overflow-hidden hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1 p-6 cursor-pointer"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 + index * 0.1 }}
              >
                {item.images && (
                  <div className="aspect-video w-full bg-black/40 rounded-lg mb-4 overflow-hidden">
                    <img
                      src={item.images}
                      alt={item.name}
                      className="w-full h-full object-cover"
                    />
                  </div>
                )}
                <h2 className="text-xl font-semibold text-white mb-3">
                  {item.name}
                </h2>
                <p className="text-gray-300 mb-4">{item.description}</p>
                <div className="text-sm text-gray-400">
                  {item.gmaps && (
                    <a
                      href={item.gmaps}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-400 hover:text-blue-300 transition-colors mt-2 inline-block"
                      onClick={(e) => e.stopPropagation()}
                    >
                      Voir sur Google Maps
                    </a>
                  )}
                </div>
              </motion.div>
            ))}
          </motion.div>

          <Modal
            isOpen={selectedItem !== null}
            onClose={() => {
              setSelectedItem(null);
              setIsMaskEnabled(true);
            }}
          >
            {selectedItem && (
              <motion.div
                className="text-white"
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.3 }}
              >
                <h2 className="text-3xl font-bold mb-4">{selectedItem.name}</h2>
                {selectedItem.images && (
                  <div className="aspect-video w-full bg-black/40 rounded-lg mb-6 overflow-hidden">
                    <img
                      src={selectedItem.images}
                      alt={selectedItem.name}
                      className="w-full h-full object-cover"
                    />
                  </div>
                )}
                <p className="text-lg text-gray-300 mb-6">
                  {selectedItem.description}
                </p>
                <div className="text-sm text-gray-400">
                  {selectedItem.gmaps && (
                    <a
                      href={selectedItem.gmaps}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-blue-400 hover:text-blue-300 transition-colors mt-2 inline-block"
                    >
                      Voir sur Google Maps
                    </a>
                  )}
                </div>
              </motion.div>
            )}
          </Modal>

          <Footer />
        </motion.div>
      </FlashlightEffect>
    </div>
  );
}
