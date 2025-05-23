interface Item {
  id: number;
  name: string;
  description: string | null;
}

interface ItemCardProps {
  item: Item;
}

export const ItemCard = ({ item }: ItemCardProps) => {
  return (
    <div className="p-8 bg-black/20 backdrop-blur-sm rounded-lg shadow-md hover:shadow-lg transition-[height,transform,box-shadow] duration-1000 ease-in-out text-white w-full hover:bg-black/10 hover:shadow-[0_0_30px_rgba(255,255,255,0.25)] text-center h-[150px] hover:h-[300px] hover:z-10 relative group">
      <h2 className="text-2xl font-semibold mb-4">{item.name}</h2>
      <p className="text-gray-200 text-lg">{item.description}</p>
      <button className="absolute bottom-4 left-1/2 -translate-x-1/2 bg-white/10 hover:bg-white/20 px-6 py-2 rounded-full transition-all duration-500 opacity-0 group-hover:opacity-100 scale-0 group-hover:scale-100">
        En savoir plus
      </button>
    </div>
  );
};
