print(*
      map(
          lambda x, y: abs(x - y),
          map(int, input().split()),
          map(int, input().split())
      )
      )
