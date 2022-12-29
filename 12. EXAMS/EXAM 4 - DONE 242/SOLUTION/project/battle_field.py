from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        bonus_hp_attacker = sum([el.health_points for el in attacker.card_repository.Cards])
        bonus_hp_enemy = sum([el.health_points for el in enemy.card_repository.Cards])

        attacker.health += bonus_hp_attacker
        enemy.health += bonus_hp_enemy

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for el in attacker.card_repository.Cards:
                el.damage_points += 30

        elif enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for el in enemy.card_repository.Cards:
                el.damage_points += 30

        # attacker engages
        dmg = sum([el.damage_points for el in attacker.card_repository.Cards])
        enemy.take_damage(dmg)
        if enemy.is_dead:
            return

        # enemy engages
        dmg = sum([el.damage_points for el in enemy.card_repository.Cards])
        attacker.take_damage(dmg)
        if attacker.is_dead:
            return
