from dataclasses import Field, dataclass
from game.phase.action_phase import ActionPhase
from game.phase.buy_phase import BuyPhase
from game.phase.closing_phase import ClosingPhase
from game.phase.start_phase import StartPhase
from player.base_player import Player


@dataclass
class PhaseHandler:
    player: Player
    opponent: Player
    field_cards: Field

    def intilize_all_phase(self):
        self.start_phase = StartPhase(self.player, self.opponent)
        self.start_phase.start_phase()
        self.start_phase.opponent_start_phase()

        self.action_phase = ActionPhase(self.player, self.opponent, self.field_cards)
        self.buy_phase = BuyPhase(self.player, self.opponent, self.field_cards)
        self.closing_phase = ClosingPhase(self.player, self.opponent)

    def handle_turn(self):
        # action phase
        self.action_phase.start_phase()

        # buy phase
        self.buy_phase.start_phase()

        # end turn
        self.closing_phase.start_phase()
        self.start_phase.start_phase()

    def swap_start_player(self):
        self.start_phase.player, self.start_phase.opponent = (
            self.start_phase.opponent,
            self.start_phase.player,
        )
        self.action_phase.player, self.action_phase.opponent = (
            self.action_phase.opponent,
            self.action_phase.player,
        )
        self.buy_phase.player, self.buy_phase.opponent = (
            self.buy_phase.opponent,
            self.buy_phase.player,
        )
        self.closing_phase.player, self.closing_phase.opponent = (
            self.closing_phase.opponent,
            self.closing_phase.player,
        )
