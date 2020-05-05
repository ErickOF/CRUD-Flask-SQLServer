SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:      Erick Andres Obregon Fonseca
-- Create date: 5th May 2020
-- Description: Return all users
-- =============================================

CREATE PROCEDURE getUsers
AS
BEGIN
    SET NOCOUNT ON;

    SELECT * FROM [user];
END
GO
