from abc import ABC, abstractmethod

import torch


class ODE(ABC):
    @abstractmethod
    def drift_coefficient(self, xt: torch.Tensor, t: torch.Tensor, **kwargs) -> torch.Tensor:
        """
        Computes the drift coefficient of the ODE.
        :param xt: state at time t, shape (bs, c, h, w)
        :param t: time, shape (bs, 1)
        :return: drift coefficient, shape (bs, c, h, w)
        """
        pass


class SDE(ABC):
    @abstractmethod
    def drift_coefficient(self, xt: torch.Tensor, t: torch.Tensor, **kwargs) -> torch.Tensor:
        """
        Computes the drift coefficient of the SDE.
        :param xt: state at time t, shape (bs, c, h, w)
        :param t: time, shape (bs, 1, 1, 1)
        :return: drift coefficient, shape (bs, c, h, w)
        """
        pass

    @abstractmethod
    def diffusion_coefficient(self, xt: torch.Tensor, t: torch.Tensor, **kwargs) -> torch.Tensor:
        """
        Returns the diffusion coefficient of the SDE.
        :param xt: state at time t, shape (bs, c, h, w)
        :param t: shape (bs, 1, 1, 1)
        :return: diffusion coefficient, shape (bs, c, h, w)
        """
        pass