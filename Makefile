.PHONY: unittest
unittest:
	pytest tests/test_car.py
	pytest tests/test_simulator.py
.PHONY: run
run:
	python3 main.py
