# progress-tracker
 Flask-based mr4mp progress tracker

```python
class Progress:
    def __init__(self, stages):
        self._status = 0
        self.stages = stages

    def hook(self, xs):  # mr4mp progress hook
        self._status = self._status + 1 % self.stages
        return xs

    def __str__(self):
        return str(round(self._status*100.0/self.stages, 2))
```

```python
progress = Progress(stages=100)  # granularity /100

mr4mp_pool.mapconcat(
    m, xs,
    progress=progress.hook,
    stages=progress.stages
)
```