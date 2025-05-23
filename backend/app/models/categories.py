from pydantic import BaseModel

class Category(BaseModel):
    """
    Représente une catégorie culturelle. 
    L'icône est un code utilisé dans Lucide Icons,
    et le champ 'primary' est le code hexadécimal de la couleur principale.
    """
    id: int
    name: str
    description: str
    icon: str
    primary: str
