"""CSC111 Project 1: Text Adventure Game - Event Logger

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

You can copy/paste your code from the ex1_simulation file into this one, and modify it as needed
to work with your game.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2025 CSC111 Teaching Team
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Event:
    """
    A node representing one event in an adventure game.

    Instance Attributes:
    - id_num: Integer id of this event's location
    - description: Long description of this event's location
    - next_command: String command which leads this event to the next event, None if this is the last game event
    - next: Event object representing the next event in the game, or None if this is the last game event
    - prev: Event object representing the previous event in the game, None if this is the first game event
    """

    # NOTES:
    # Complete this class EXACTLY as specified, with ALL of the above attributes.
    # Do NOT add any new attributes, or modify the names or types of the above attributes.
    # If you want to create a special type of Event for your game that requires a different
    # set of attributes, you can do that separately in the project1 folder. This class is part of
    # Exercise 1 and will be auto-graded.

    id_num: int
    description: str
    next_command: Optional[str] = None
    next: Optional['Event'] = None
    prev: Optional['Event'] = None


class EventList:
    """
    A linked list of game events.

    Instance Attributes:
         - first: The first event in the event list, or None if the list is empty.
        - last: The last event in the event list, or None if the list is empty.

    Representation Invariants:
        - If first is None, then last must also be None (the list is empty).
        - If first is not None, the list should be linked from first to last.
    """
    first: Optional[Event]
    last: Optional[Event]

    def __init__(self) -> None:
        """Initialize a new empty event list."""

        self.first = None
        self.last = None

    def display_events(self) -> None:
        """Display all events in chronological order."""
        curr = self.first
        while curr:
            print(f"Location: {curr.id_num}, Command: {curr.next_command}")
            curr = curr.next

    def is_empty(self) -> bool:
        """Return whether this event list is empty."""

        return self.first is None

    def add_event(self, event: Event, command: Optional[str] = None) -> None:
        """Add the given new event to the end of this event list.
        The given command is the command which was used to reach this new event, or None if this is the first
        event in the game.

         >>> event_list = EventList()
        >>> event1 = Event(1, "Start of the game")
        >>> event2 = Event(2, "Find the key")
        >>> event_list.add_event(event1)
        >>> event_list.add_event(event2, "go north")
        >>> event_list.first.id_num
        1
        >>> event_list.last.id_num
        2
        >>> event_list.last.prev.id_num
        1
        >>> event_list.last.next_command
        'go north'
        """
        # Hint: You should update the previous node's <next_command> as needed
        # DOCTESTS GENERATED FROM CHATGPT FOR TESTING AND DEBUGGING PURPOSES
        if self.is_empty():
            self.first = event
            self.last = event
            event.prev = None
            event.next_command = None
        else:
            self.last.next = event  # pointer of last node will now point to the new event
            event.prev = self.last
            event.next_command = command
            self.last = event

    def remove_last_event(self) -> None:
        """Remove the last event from this event list.
        If the list is empty, do nothing.
         # DOCTESTS GENERATED FROM CHATGPT FOR TESTING AND DEBUGGING PURPOSES
         >>> event_list = EventList()
        >>> event1 = Event(1, "Start of the game")
        >>> event2 = Event(2, "Find the key")
        >>> event_list.add_event(event1)
        >>> event_list.add_event(event2, "go north")
        >>> event_list.remove_last_event()
        >>> event_list.last.id_num
        1
        >>> event_list.last.next is None
        True
        >>> event_list.remove_last_event()
        >>> event_list.is_empty()
        True
            """

        # Hint: The <next_command> and <next> attributes for the new last event should be updated as needed
        #  DOCTESTS GENERATED FROM CHATGPT FOR TESTING AND DEBUGGING PURPOSES
        if not self.is_empty():
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.last = self.last.prev
                self.last.next = None
                self.last.next_command = None

    def get_id_log(self) -> list[int]:
        """Return a list of all loc ation IDs visited for each event in this list, in sequence.
            >>> event_list = EventList()
            >>> event1 = Event(1, "Start of the game")
            >>> event2 = Event(2, "Find the key")
            >>> event3 = Event(3, "Unlock the gate")
            >>> event_list.add_event(event1)
            >>> event_list.add_event(event2)
             >>> event_list.add_event(event3)
            >>> event_list.get_id_log()
            [1, 2, 3]
        """

        id_log = []
        current = self.first
        while current is not None:
            id_log.append(current.id_num)
            current = current.next
        return id_log
    # Note: You may add other methods to this class as needed but DO NOT CHANGE THE SPECIFICATION OF ANY OF THE ABOVE
    # DOCTESTS GENERATED FROM CHATGPT FOR TESTING AND DEBUGGING PURPOSES


if __name__ == "__main__":
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['R1705', 'E9998', 'E9999']
    })
