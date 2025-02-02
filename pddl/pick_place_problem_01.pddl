(define (problem pick_and_place_problem_01)
  (:domain pick_and_place)

  (:objects
    bin_1 bin_2 bin_3 - bin
    part_1 part_2 - part
  )

  (:init
    (robot_at bin_3)
    (gripper_empty)
    (part_at part_1 bin_1)
    (part_at part_2 bin_2)
    (occupied bin_1)
    (occupied bin_2)
  )

  (:goal
    (and 
        (robot_at bin_2)
        (part_at part_1 bin_3)
        (part_at part_2 bin_1)
	)
  )
)