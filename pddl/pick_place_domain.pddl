(define (domain pick_and_place)
    (:types
        bin
        part
    )

    (:predicates
        (robot_at ?b - bin)
        (part_at ?p - part ?b - bin)
        (holding ?p - part)
        (gripper_empty)
        (occupied ?b - bin)
    )

    (:action move
        :parameters (?b_from - bin ?b_to - bin)
        :precondition (and 
            (robot_at ?b_from)
        )
        :effect (and
            (not (robot_at ?b_from))
            (robot_at ?b_to)
        )
    )

    (:action pick
        :parameters (?p - part ?b - bin)
        :precondition (and 
            (robot_at ?b)
            (part_at ?p ?b)
            (gripper_empty)
        )
        :effect (and
            (not (part_at ?p ?b))
            (holding ?p)
            (not (gripper_empty))
            (not (occupied ?b))
        )
    )

    (:action place
        :parameters (?p - part ?b - bin)
        :precondition (and 
            (robot_at ?b)
            (holding ?p)
            (not (occupied ?b))
        )
        :effect (and
            (not (holding ?p))
            (gripper_empty)
            (part_at ?p ?b)
            (occupied ?b)
        )
    )

)