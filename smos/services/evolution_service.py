from sqlalchemy.orm import Session
from smos.models.experience import Recipe, Wisdom, RecipeExecution
from typing import List, Dict, Any

class EvolutionService:
    def __init__(self, db: Session):
        self.db = db

    def evolve_recipe(self, parent_id: int, mutations: List[Dict[str, Any]]):
        parent = self.db.query(Recipe).get(parent_id)
        if not parent:
            return None

        # Create mutated descendant
        new_recipe = Recipe(
            title=f"{parent.title} (Evolved)",
            description=parent.description,
            author_id=parent.author_id,
            problem_type=parent.problem_type,
            steps=parent.steps, # This would be modified by mutations in a real system
            parent_recipe_id=parent_id,
            mutations=mutations
        )
        self.db.add(new_recipe)
        self.db.commit()
        self.db.refresh(new_recipe)
        return new_recipe

    def distill_wisdom(self, recipe_id: int):
        """Aggregate successful executions into Wisdom"""
        executions = self.db.query(RecipeExecution).filter(
            RecipeExecution.recipe_id == recipe_id,
            RecipeExecution.result == "SUCCESS"
        ).all()

        if len(executions) >= 3: # Criteria for 'Wisdom'
            recipe = self.db.query(Recipe).get(recipe_id)
            wisdom = Wisdom(
                recipe_id=recipe_id,
                domains=[recipe.problem_type],
                confidence=0.9,
                evidence={"execution_count": len(executions)}
            )
            self.db.add(wisdom)
            self.db.commit()
            self.db.refresh(wisdom)
            return wisdom
        return None
